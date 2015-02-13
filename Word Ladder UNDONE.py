class TreeNode:
    def __init__(self,parent,value=None):
        self.parent     =  parent
        self.value      =  value
        self.childList  =  []
    
    def parents(self):
        ret=[]
        while self.parent:
            ret.append(self.parent.value)
            self=self.parent
        return ret
    
    def show(self):
        print self.value
        if self.childList:
            print '-'
            for x in self.childList:
                x.show()

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        lists=list(dict)

        prev=[start]
        dept=0
        for x in prev:

        next_lists=self.next(prev)

    def next_lists(self,prev):
        for x in prev:
            next_lists.

    def ladderLength(self, start, end, dict):
        lists=list(dict)
        lists.append(start)
        lists.append(end)
        
        head=TreeNode(None,start)
        childs=self.next(head.value,lists)
        if len(childs)==0:
            return 0
        if end in childs:
            return 2
        for x in childs:
            head.childList.append(TreeNode(head,x))

        return self.get_childs_recur(head,lists,end,2)
        
        
        
        
    def get_childs_recur(self,parent,dicts,end,dept):
        dept+=1
        for child in parent.childList:
            temp=list(dicts)
            for p in child.parents():
                if p in temp:
                    temp.remove(p)
                
            childs=self.next(child.value,temp)
            if len(childs)!=0:
                print dept
                if end in childs:
                    return dept
                for x in childs:
                    child.childList.append(TreeNode(child,x))
                
        for child in parent.childList:
            return self.get_childs_recur(child,dicts,end,dept)
        return 0
    
    def next(self,check,dict):
        ret=[]
        for x in dict:
            same_ch_num=0
            for i in range(len(x)):
                if x[i]==check[i]:
                    same_ch_num+=1
            if same_ch_num==len(check)-1:
                ret.append(x)
        return ret
        
a=Solution()
print a.ladderLength("nape", "mild", ["dose","ends","dine","jars","prow","soap","guns","hops","cray","hove","ella","hour","lens","jive","wiry","earl","mara","part","flue","putt","rory","bull","york","ruts","lily","vamp","bask","peer","boat","dens","lyre","jets","wide","rile","boos","down","path","onyx","mows","toke","soto","dork","nape","mans","loin","jots","male","sits","minn","sale","pets","hugo","woke","suds","rugs","vole","warp","mite","pews","lips","pals","nigh","sulk","vice","clod","iowa","gibe","shad","carl","huns","coot","sera","mils","rose","orly","ford","void","time","eloy","risk","veep","reps","dolt","hens","tray","melt","rung","rich","saga","lust","yews","rode","many","cods","rape","last","tile","nosy","take","nope","toni","bank","jock","jody","diss","nips","bake","lima","wore","kins","cult","hart","wuss","tale","sing","lake","bogy","wigs","kari","magi","bass","pent","tost","fops","bags","duns","will","tart","drug","gale","mold","disk","spay","hows","naps","puss","gina","kara","zorn","boll","cams","boas","rave","sets","lego","hays","judy","chap","live","bahs","ohio","nibs","cuts","pups","data","kate","rump","hews","mary","stow","fang","bolt","rues","mesh","mice","rise","rant","dune","jell","laws","jove","bode","sung","nils","vila","mode","hued","cell","fies","swat","wags","nate","wist","honk","goth","told","oise","wail","tels","sore","hunk","mate","luke","tore","bond","bast","vows","ripe","fond","benz","firs","zeds","wary","baas","wins","pair","tags","cost","woes","buns","lend","bops","code","eddy","siva","oops","toed","bale","hutu","jolt","rife","darn","tape","bold","cope","cake","wisp","vats","wave","hems","bill","cord","pert","type","kroc","ucla","albs","yoko","silt","pock","drub","puny","fads","mull","pray","mole","talc","east","slay","jamb","mill","dung","jack","lynx","nome","leos","lade","sana","tike","cali","toge","pled","mile","mass","leon","sloe","lube","kans","cory","burs","race","toss","mild","tops","maze","city","sadr","bays","poet","volt","laze","gold","zuni","shea","gags","fist","ping","pope","cora","yaks","cosy","foci","plan","colo","hume","yowl","craw","pied","toga","lobs","love","lode","duds","bled","juts","gabs","fink","rock","pant","wipe","pele","suez","nina","ring","okra","warm","lyle","gape","bead","lead","jane","oink","ware","zibo","inns","mope","hang","made","fobs","gamy","fort","peak","gill","dino","dina","tier"])

# t=TreeNode(None,1)
# t1=TreeNode(t,2)
# t2=TreeNode(t1,3)
# t.childList=[t1]
# t1.childList=[t2]
# print t2.parents()