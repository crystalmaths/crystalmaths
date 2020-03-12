#define the needed functions
#take one input that's a list to be able to have a variable number of dspacings
def make_web_address(dspacing1, dspacing2):
    '''
    make_web_address will compile a string to use for a webpage address
    
    For example, if I want to search for rutile on the American 
    Minerals Society webpage, I might use this address:
    
    http://rruff.geo.arizona.edu/AMS/result.php?diff=vals(3.2435,2.4836),opt(),type(d-spacing),tolerance(.001)
    
    Where 3.2435 and 2.4836 are two d spacings in the rutile structure
    '''
    
    web_address = 'http://rruff.geo.arizona.edu/AMS/result.php?diff=vals(' + str(dspacing1) + ',' + str(dspacing2) +'),opt(),type(d-spacing),tolerance(.001)'
    
    return web_address

def find_diffraction_files(href):
    '''
    find_diffraction_files is a sorting function that can be passed 
    into compile_links to generate a specific set of diffraction text 
    file web addresses from the American Mineral Society database
    
    find_diffraction_files works together with compile_links
    '''
# commented out logic will return the text file links
#     return href and re.compile("txt").search(href) and not re.compile("dif").search(href)        
    return href and re.compile("dif").search(href)        

def compile_links(web_address):
    '''
    compile_links accesses a webpage at a given address,
    finds all of the links on that page, and appends certain links 
    to a list called links_list.
    
    compile links works together with find_diffraction_files to 
    get only the relevant links.
    
    inputs are a web address, and the list for storing links
    '''
    
    html_page = requests.get(web_address)
    http_encoding = html_page.encoding if 'charset' in html_page.headers.get('content-type', '').lower() else None
    html_encoding = EncodingDetector.find_declared_encoding(html_page.content, is_html=True)
    encoding = html_encoding or http_encoding
    soup = BeautifulSoup(html_page.content, from_encoding=encoding)
    links_list = []
    for link in soup.find_all(href=find_diffraction_files):
        links_list.append('http://rruff.geo.arizona.edu'+link['href'])
    
    return links_list

def split_diffraction_data(link):
    '''
    get_diffraction_data will compile crystal structure parameters and 
    indexes of all potential planes into a pandas DataFrame
    
    Inputs are an array of truncated href, two d spacings from the FFT, 
    and the pandas DataFrame into which data will be stored. Returns the
    populated DataFrame.
    '''

    with requests.Session() as s:
        download = s.get(link)
        decoded_content = download.content.decode('utf-8')
        metadata_list = []
        reader = csv.reader(decoded_content.splitlines())
        raw_data_list = []
        for i, row in enumerate(reader):
            #This is for handling [], empty rows
            if len(row) != 0:
                entry = row[0]
                entry.split()
                raw_data_list.append(entry)
                string = row[0]
            if string.find('2-THETA') != -1:
                metadata_end_index = i
            elif string.find('==============================') != -1:
                data_end_index = i
            else:
                pass
                
        metadata_list = raw_data_list[0:metadata_end_index-1]
        data_list = raw_data_list[metadata_end_index-1:data_end_index-1]
    return (metadata_list, data_list)

def sort_lists(link):
    '''
    sort_lists is a function that returns formated data aquired from
    the American Mineral Society for analysis
    
    inputs are a tuple of two lists, one containing metadata and one 
    containing diffraction data.  
    These lists come from the split_diffraction_data function
    
    the output is a tuple of three lists containing our 
    desired metadata, our data labels, and diffraction data 
    
    desired metadata: Mineral Name, Space Group, Cell Parameters 
    '''
    metadata_list, data_list = split_diffraction_data(link)
    structure_list = [metadata_list[0]]
    data_labels = [data_list[0].split()]
    clean_data_list = []
    #this loop works through the metadata and 
    #extracts the values that we want  
    #currently we have strings containing what we want and 
    #they need to be processed further to remove whitespace, 
    #cell paramaters need to be split up, 
    #extra label text needs to be removed, and 
    #strings of numbers need to be converted to floats

    for row in metadata_list:
        string = row
        entry = row
        if string.find('SPACE') != -1:
            structure_list.append(entry)
        if string.find('PARAMETERS') != -1:
            structure_list.append(entry)
    #print(structure_list) 

    #this loop works through the actuall data and 
    #extracts the rows with d spacing close to measured values from fft
    #needs to split the rows,
    #convert the strings of numbers into floats,
    #compile the rows which contain d spacings close to measured values from fft
    #remove extra data that we don't need to only keep d spacing and h k l values
    del data_list[0] #this command is removing the labels, which have been stored in a separate list
    for row in data_list:
        string = row
        entry = string.split()
        clean_row = []
        for item in entry:
            item = float(item)
            clean_row.append(item)
        clean_data_list.append(clean_row)
    return structure_list, data_labels, clean_data_list

    

def lists_to_dfs(link):
    '''
    lists_to_dfs generates pandas dataframes for the data and metadata 
    '''
    structure_list, data_labels, clean_data_list = sort_lists(link)
    mineral = structure_list[0]
    metadata_dict = {'Mineral_Name': mineral.strip()}
    cell_params = structure_list[1]
    cell_params_list = cell_params.split()
    del cell_params_list[0:2]#here i want to remove all list entries with a non digit \D
    cell_params_labels = ['a','b','c','alpha', 'gamma', 'beta']
    i = 0
    for entry in cell_params_labels:
        label = cell_params_labels[i]
        entry = cell_params_list[i]
        metadata_dict.update({label:[entry]})
        i = i + 1
    metadata_df = pd.DataFrame(metadata_dict)
    diffraction_df = pd.DataFrame(clean_data_list, columns=data_labels[0])
    diffraction_df = diffraction_df[['D-SPACING', 'H', 'K', 'L']]
    return metadata_df, diffraction_df

def select_data(link, d_spacing_list):
    '''
    select_data compiles a new dataframe from the diffraction data
    containing only the rows with relevant data to our search 
    '''
    metadata_df, diffraction_df = lists_to_dfs(link)
    structure_df = pd.DataFrame()
    for entry in d_spacing_list:
        d_spacing_df = diffraction_df.loc[np.isclose(diffraction_df['D-SPACING'], entry, atol=.1)]
        structure_df = structure_df.append(d_spacing_df)
#    crystalmaths_df = pd.concat([metadata_df, structure_df], axis=1, ignore_index=True)
    return structure_df, metadata_df


def get_d(links_list, d_spacing_list):
    crystalmaths_master_list = []
    for link in links_list:
        mineral_tuple = (select_data(link, d_spacing_list))
        crystalmaths_master_list.append(mineral_tuple)
    return crystalmaths_master_list
