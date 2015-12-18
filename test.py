import sys
import os

def wirteFile(filename,output):
	fopen = open(filename,'w')

	fopen.write(output)

	fopen.close()

def get_commit_file_list(rev,repo):

	cmd = '%s changed -r %s %s' % (svnlook_bin_path, rev, repo)
	print cmd
	return cmd

def execCmd(cmd):
        r = os.popen(cmd)
        text = r.read()
        r.close()
        return text




global svnlook_bin_path
if __name__ == '__main__':
	svnlook_bin_path = "svnlook"
	t1 = sys.argv[1]
	t2 = sys.argv[2]
	cmd=get_commit_file_list(t2,t1)
	output = execCmd(cmd)
	wirteFile('updatefile.txt',output)
