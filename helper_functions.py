import numpy as np

def labels_from_df(sel_data,im_shape,label,image,bbox_suffix=None):
    
    '''
    Function to create labels based on the df
    
    input:
        df - with bbox and label info
        im_shape - size of the canvas
    
    output:
        labels
    '''
    
    row_total = im_shape[0]
    column_total = im_shape[1]

    # create an empty image
    label_image = np.zeros([row_total,column_total]).astype('uint16')
    
    # add objects
    for ind,my_cell in sel_data.iterrows():
        
        if (my_cell[label] == my_cell[label]): #if it's a real object

            min_row = int(my_cell[f'bbox-0{bbox_suffix}'])
            max_row = int(my_cell[f'bbox-2{bbox_suffix}'])
            min_col = int(my_cell[f'bbox-1{bbox_suffix}'])
            max_col = int(my_cell[f'bbox-3{bbox_suffix}'])
    
            label_image[min_row:max_row,min_col:max_col]=label_image[min_row:max_row,min_col:max_col]+(my_cell[image]*my_cell[label])
                                   

    return label_image