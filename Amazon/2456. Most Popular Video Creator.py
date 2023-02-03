class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        d={}
        for i in range(len(creators)):
            cid,vid,view=creators[i],ids[i],views[i]
            if(cid not in d):
                d[cid]={'totalViewCount':0, 'videoList':[]}
            d[cid]['totalViewCount']+=view
            d[cid]['videoList'].append((view,vid))
        clist=[(d[cid]['totalViewCount'],cid) for cid in d]
        clist.sort(reverse=True)
        maxView=clist[0][0]
        ans=[]
        for totalView,cid in clist:
            if(totalView!=maxView):
                break
            t=d[cid]['videoList']
            t.sort(reverse=True)
            mx=t[0][0]
            for view,vid in t:
                if(view!=mx):
                    break
                v=vid
            ans.append([cid,v])
        return ans