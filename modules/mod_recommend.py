#coding=utf8
import sys
import json
import global_var 
sys.path.append(sys.path[0])


#user dict for test
user_dict={}
user_dict['tangning']=[]
user_dict['tangning'].append('股票'.decode('utf8'))
user_dict['yixin']=[]
user_dict['yixin'].append('篮球'.decode('utf8'))
user_dict['hanwu']=[]
user_dict['hanwu'].append('房产'.decode('utf8'))

def service(request):
  #query=request.form.get('query','')
  type=request.args.get('type','')
  if type=='key_word':
    print "recommend for keyword!"
    query=request.args.get('query','')
    if query != '':
      source=[]
      source.append(query)
      similars=global_var.MODEL.most_similar(positive=source,negative=[],topn=5)
      recommend={}
      recommend['recommend_type']='query'
      recommend['result']='true'
      recommend['data']=[]
      for similar in similars:
        recommend['data'].append(similar[0])
        print similar[0]
      return_string=json.dumps(recommend,ensure_ascii=False)
      print return_string
      return return_string
  elif type=='user': 
    print "recommend for user!"
    name=request.args.get('name','')
    if name != '':
      recommend={}
      recommend['recommend_type']='user'
      recommend['result']='true'
      recommend['data']=user_dict[name]
      return_string=json.dumps(recommend,ensure_ascii=False)
      print return_string
      return return_string
  else:
    return ""
