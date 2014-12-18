#Compare Version Numbers
#问题描述
#Compare two version numbers version1 and version1.
#版本号对比
#思路:拆成数组比对，关键在填0和转换为整型比较大小

class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        versionList1=version1.split('.')
        versionList2=version2.split('.')

        versionList1=map(lambda x:int(x),versionList1)
        versionList2=map(lambda x:int(x),versionList2)

        l1=len(versionList1)
        l2=len(versionList2)

        for k in range(max([l1,l2])):
            #填充0
            if k+1>l1:
                versionList1.append(0)
            if k+1>l2:
                versionList2.append(0)

            if versionList1[k]>versionList2[k]:
                return 1
            elif versionList1[k]<versionList2[k]:
                return -1
            if k+1==max([l1,l2]):
                return 0

a=Solution()
print a.compareVersion('1','1.1')