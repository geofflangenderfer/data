import gzip
import shutil


def zip_files(files):

    for f in data_files:
        with open(f, 'rb') as f_in, gzip.open(f+'.gz','wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
def unzip_file(f):
    name = f.split('.')[0] + '.csv'

    with gzip.open(f, 'rb') as f_in:
        with open(name, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

if __name__ == '__main__':
    # unzip
#    data_files = ['sample_submission.csv', 'stack_network_links.csv',
#                  'stack_network_nodes.csv', 'test.csv', 'train.csv']
#    data_files = [x+'.gz' for x in data_files]
#    for f in data_files:
#        unzip_file(f)
    
    # zip
    data_files = ['sample_submission.csv', 'stack_network_links.csv',
                  'stack_network_nodes.csv', 'test.csv', 'train.csv']
    zip_files(data_files)
