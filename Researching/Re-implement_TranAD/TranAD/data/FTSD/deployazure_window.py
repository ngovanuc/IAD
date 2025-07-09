"""
Tự động tạo 2 máy ảo (VM) trên Azure, cài kernel, cấu hình diagnostic logging và tạo tài khoản lưu 
trữ (Azure Storage Account) để nhận dữ liệu.
"""
import subprocess
from time import sleep
import json

# Create two Azure VMs with specified names and sizes
# Ensure you have the Azure CLI installed and configured with your account
vmlist = [('vm1', 'Standard_B2ms'), ('vm2', 'Standard_B2ms')]

# Thực hiện lệnh Azure CLI qua terminal
def run(cmd, shell=True):
  data = subprocess.run(cmd, shell=shell, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  if b'ERROR' in data.stderr:
    print(cmd)
    print(data.stderr.decode())
    exit()
  return data.stdout.decode()

print('Create Azure VM')
for name, size in vmlist:
  run(f'az vm create --resource-group vm1_group --name {name} --size {size} --image UbuntuLTS --ssh-key-values id_rsa.pub --admin-username ansible')

print('Wait for deployment (1 minute)')
sleep(60)

print('Open port 8081')
for name, size in vmlist:
  run(f'az vm open-port --resource-group vm1_group --name {name} --port 8081')

print('Install new kernel')
for name, size in vmlist:
  cmd = (
    'az vm run-command invoke -g vm1_group -n {name} --command-id RunShellScript '
    '--scripts "sudo apt install -y -f linux-image-4.15.0-1009-azure linux-tools-4.15.0-1009-azure '
    'linux-cloud-tools-4.15.0-1009-azure linux-headers-4.15.0-1009-azure '
    'linux-modules-4.15.0-1009-azure linux-modules-extra-4.15.0-1009-azure"'
  ).format(name=name)
  run(cmd)

print('Deallocate VMs')
for name, size in vmlist:
  run(f'az vm deallocate --resource-group vm1_group --name {name}')

print('Update Disks')
data = run("az disk list --resource-group vm1_group")
print('Disk list:', data)
try:
  d = json.loads(data)
except Exception as e:
  print("Failed to parse disk list:", e)
  exit()
for a in d:
  disk_id = a['id'].split('/')[-1]
  run(f'az disk update --name {disk_id} --resource-group vm1_group --size-gb 256 --set tier=P15')

print('Start VMs')
for name, size in vmlist:
  run(f'az vm start --resource-group vm1_group --name {name}')

print('Create storage account')
run('az storage account create --name shreshthstorage --resource-group vm1_group --access-tier Hot --kind StorageV2 --location uksouth --sku Standard_RAGRS')

print('Set diagnostic info')
sas_token = run('az storage account generate-sas --account-name shreshthstorage --expiry 2037-12-31T23:59:00Z --permissions wlacu --resource-types co --services bt -o tsv')
sas_token = sas_token.strip()
p_settings = json.dumps({
  "storageAccountName": "shreshthstorage",
  "storageAccountSasToken": sas_token
})
with open('diagnostic.json') as f:
  setting = json.load(f)
for name, size in vmlist:
  setting['ladCfg']['resourceId'] = name
  sett = json.dumps(setting)
  cmd = (
    f'az vm diagnostics set --settings "{sett}" --protected-settings "{p_settings}" '
    f'--resource-group vm1_group --vm-name {name}'
  )
  run(cmd)
