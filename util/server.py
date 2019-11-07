#encoding:utf-8
from dos_com import DosCmd
from port import Port
import threading
from yamlConfig import YamlClss

class Server:
    def __init__(self):
        self.dos = DosCmd()
        self.devices_list=self.get_device()
        self.myYaml = YamlClss()
    #获取设备信息
    def get_device(self):
        devices_list=[]
        result_list=self.dos.excute_com_result('adb devices')
        if len(result_list)>=2:
            for i in result_list:
                if 'List' in i:
                    continue
                devices=i.split('\t')[0]
                devices_list.append(devices)
            return devices_list
        else:
            return None
    #生成端口列表
    def create_port_list(self,start_port):
        port=Port()
        port_list=port.create_port_list(start_port,self.devices_list)
        return port_list

    #生成启动命令
    def create_command_list(self,i):
        command_list=[]
        appium_port_list=self.create_port_list(4700)
        bp_port_list=self.create_port_list(4900)
        device_list=self.devices_list
        command="appium -p "+str(appium_port_list[i])+" -bp "+str(bp_port_list[i])+" -U "+device_list[i]+" --no-reset --session-override"
        command_list.append(command)
        self.myYaml.write_date(i,device_list[i],str(bp_port_list[i]),appium_port_list[i])
        return command_list

    #根据命令启动appium
    def start_server(self,i):
        self.start_list=self.create_command_list(i)
        print self.start_list
        self.dos.excute_com(self.start_list[0])

    #杀appium进程
    def kill_sercer(self):
        server_list=self.dos.excute_com_result("tasklist | find 'node.exe'")
        if len(server_list)>0:
            self.dos.excute_com('taskkill -F -PID node.exe')

    #多线程启动appium的mian方法
    def main(self):
        self.myYaml.clear_data()
        self.kill_sercer()
        for i in range(len(self.devices_list)):
            appium_start=threading.Thread(target=self.start_server,args=(i,))
            appium_start.start()
            print i




if __name__ == '__main__':
    server=Server()
    print server.main()

