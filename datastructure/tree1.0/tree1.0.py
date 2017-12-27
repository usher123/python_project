import pickle
import os
from img import find_son , find_deepth
class define:
    def info_creat(self,use):
        use.setdefault(self.name,{})['mother'] = raw_input('mother\'s name:')
        use.setdefault(self.name,{})['father'] = raw_input('father\'s name:') 
        use.setdefault(self.name,{})['son'] = [raw_input('son\'s name:')]
        ouf = open('info.json','w')
        pickle.dump(use,ouf,0)
        ouf.close()
        
    def info_name(self,use):
        self.name = raw_input("ok here we go! the name:")
        if self.name not in use:
           self.info_creat(use)
        else:
            print('have existed.')
            if raw_input('creat new one:1,exit :2\t') == '1':
                self.name = self.name + '*'
                self.info_creat(use)
            else:
                print('next people')
                pass

        
    def to_del(self,use):
        self.name = raw_input('input del name:')
        a = use.pop(self.name,None)
        if a != None:
            print( 'to del success')
        else:
            print('None this people\n')
        ouf = open('info.json','w')
        pickle.dump(use,ouf,0)
        ouf.close()

    def to_print_son(self,use):
        b = find_son(use)
        find_deepth(b,use)

    def to_check(self,use):
        print use
        self.name = raw_input('\nto input check name\n:')
        '''b = use.get(self.name)'''
        if use.get(self.name) != None:
            '''_next = raw_input('to input check name:\t\texit:0\n:')'''
            while self.name != '0':
                print(use.get(self.name,0)) #if not get name,well result is 0
                self.name = raw_input('please continue(name) or exit(0):')
                
        else:
            print('None this people!\n')
            


def new():
    json_none = open('info.json','rb')
    want = raw_input('creat new json? yes or no:\t')

    if ((want == 'yes') or (json_none.read() == '')):
        print('push \'ctrl + d\' to complete')
        os.system('cat > info.json')
        a = dict()
        b = open('info.json','w')
        pickle.dump(a,b,0)
        b.close()
    else:
        pass

if __name__ == "__main__":
    new()
    b = define()
    deal_dict = {'1':b.info_name,'2':b.to_del,'3':b.to_print_son,'4':b.to_check}
    go =raw_input('creat:1,\t del:2\nprint_son:3,\t check:4\nexit:5\n:')
    while go != '5':
        ouf = open('info.json','r')

        use = pickle.load(ouf)
        try:
            deal_dict[go](use)
        except:
            pass
        go =raw_input('continue to creat:1,\t del:2\nprint_son:3,\t\t check:4\nexit:5\n:')
            
    print('bye-bye')
