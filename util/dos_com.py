#encoding:utf-8
import os

class DosCmd:
    def excute_com_result(self,command):
        result_list=[]
        result=os.popen(command).readlines()
        for i in result:
            if i=='\n':
                continue
            result_list.append(i.strip('\n'))
        return result_list

    def excute_com(self,command):
        os.system(command)


if __name__ == '__main__':
    dos=DosCmd()
    # dos.excute_com('appium -p 4700 -bp 4900 -U 127.0.0.1:21503 --no-reset --session-override')
    print dos.excute_com_result("ll")


