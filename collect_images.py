#!/usr/bin/env python

import os
import os.path as osp

post_dir = '_posts/'
image_dir = 'Galerie.markdown'

filenames = os.listdir(post_dir)

filename_images = {}
for filename in filenames[::-1]:
    if not filename.endswith('.markdown'):
        continue
    total_images = []
    with open(osp.join(post_dir, filename), 'r') as f:
        try:
            multiline=''
            for line in f:
                if multiline and (line.startswith('</figure>') or line.startswith('</style>')) :
                    multiline += line[:-1] # skip new line
                    total_images.append(multiline)
                    multiline = ''
                elif multiline:
                    multiline += line
                elif line.startswith('!['):
                    total_images.append(line[:-1]) # skip new line
                elif line.startswith('<figure>') or line.startswith('<style>'):
                    multiline += line # include new line
        except UnicodeDecodeError:
            print('ERROR: {}, {}'.format(osp.join(post_dir, filename), line))
            continue
    if len(total_images) > 0:
        filename_images[filename.replace('.markdown', '')] = []
        for ti in total_images:
            filename_images[filename.replace('.markdown', '')].append(ti)

if not os.path.exists(image_dir):
    os.makedirs(image_dir)
    
with open(image_dir, 'w') as out:
    header_str = '---\nlayout: page\ntitle: Images\npermalink: /Galerie/\n---\n\n'
    out.write(header_str)
    for fn in filename_images.keys():
        for imn in filename_images[fn][::-1]:
            if imn.startswith('!['):
                write_str = '[{}]({{% post_url {} %}})\n'.format(imn, fn)
            elif imn.startswith('<style>'):
                write_str = imn
            else:
                write_str = '<p>\n<a href="{{% post_url {} %}}" title="Redirect to blogpage">\n{}</a></p>\n'.format(fn, imn)
            out.write(write_str)
print("Images generated")





























