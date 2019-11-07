#coding=utf-8
from dos_com import DosCmd
class Port:
    def check_port(self,port):
        self.dos=DosCmd()
        result=self.dos.excute_com_result('netstat -ano | findstr '+str(port))
        if len(result)>0:
            return  True
        else:
            return False
    def create_port_list(self,start_port,device_list):
        port_list=[]
        if len(device_list)>0:
            while len(port_list)!=len(device_list):
                if self.check_port(start_port)!=True:
                    port_list.append(start_port)
                start_port = start_port + 1
            return port_list
        else:
            print '生成可用端口失败'
            return None



if __name__ == '__main__':
    port=Port()
    # print port.check_port('8080')
    list=[]
    print port.create_port_list(4723,list)

