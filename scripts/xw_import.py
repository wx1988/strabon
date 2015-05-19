import os

SW_ROOT = '/home/xingwang/semnet'
def import_one(fpath):
    cmd = './strabon -c strabon_iswc.conf store -f n3 %s'%(fpath)
    cmd = cmd.replace('(','\\(')
    cmd = cmd.replace(')','\\)')
    print cmd
    os.system(cmd)


def import_sigacts():
    nt_dir = '%s/formatevent/res'%(SW_ROOT)
    flist = os.listdir(nt_dir)
    for fname in flist:
        print fname
        if not fname.endswith('nt'):
            continue
        fpath = nt_dir+'/'+fname
        import_one(fpath)

if __name__ == "__main__":
    import_sigacts()
    import_one('%s/format_amenity/amenity.nt'%(SW_ROOT))
    import_one('%s/afgeth/ethno.nt'%(SW_ROOT))

