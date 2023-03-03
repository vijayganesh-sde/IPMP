class Solution:
    def frequencySort(self, nums) :
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        d=dict(sorted(d.items(), key=lambda item: item[1]))
        d1={}
        for key in d:
            if d[key] not in d1:
                d1[d[key]]=[key]
            else:
                d1[d[key]].append(key)
        print(d1)
        nums=[]
        for key in d1:
            d1[key].sort(reverse=True)
            for val in d1[key]:
                nums.extend(key*[val])
        return nums