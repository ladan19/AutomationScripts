import ijson, subprocess

input_file_name = 'output.json'
vault_name = ''
account_id = ''

f = open(input_file_name)
archive_list = ijson.items(f,'ArchiveList.item')

for archive in archive_list:
    print("Deleting archive " + archive['ArchiveId'])
    command = "aws glacier delete-archive --archive-id='" + archive['ArchiveId'] + "' --vault-name " + vault_name + " --acc$
    subprocess.run(command, shell=True, check=True)

f.close()
