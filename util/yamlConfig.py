#encoding:utf-8
import yaml
import os,sys
reload(sys)

class YamlClss:
    def read_data(self):
        #加载数据
        with open('../config/dirver.yaml') as fr:
            data=yaml.safe_load(fr)
        return data
    #写入yaml数据
    def write_date(self,i,device,bp,port):
        data=self.join_data(i,device,bp,port)
        with open('../config/dirver.yaml','a') as fr:
            yaml.dump(data,fr)

    #获取数据
    def get_value(self,key,key2):
        data=self.read_data()
        value=data[key][key2]
        return value

    #拼接参数
    def join_data(self,i,device,bp,port):
        data={
            "server_"+str(i):{
            "device":device,
            "bp":bp,
            "port":port
        }
        }
        return data
    #清空数据
    def clear_data(self):
        with open('../config/dirver.yaml', 'w') as fr:
            fr.truncate()
        fr.close()



if __name__ == '__main__':
    yamls=YamlClss()
    print yamls.get_value('server_1','port')