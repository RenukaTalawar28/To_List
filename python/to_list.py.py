from flask import Flask,request,jsonify
app = Flask(__name__)

datastore=[]
i=0

@app.route('/',methods=['GET'])
def getall():
    # 'isComplted'=False
    return jsonify(datastore)

@app.route('/addtodo',methods=['POST'])
def add(): 
   item=request.json
   global i
   item['id']=i+1
   item['isComplted']=False
   i+=1
   if item not in datastore:
    datastore.append(item)
    return item
   

@app.route('/update',methods=['POST'])
def update_todo():
  update=request.json
  if update['id']<=len(datastore):
   for i in datastore:
    if i['id']==update['id']:
      i['isComplted']=True
      return i
  return jsonify(msg="invalid id")    


@app.route('/delete',methods=['POST'])
def delete_todo():
  delete=request.json
  if delete['id']<=len(datastore):
   for index,i in enumerate(datastore):
     if i['id']==delete['id']and i['isComplted']==True:
       del(datastore[index])
       return jsonify(msg="succusesfully delted")
     return jsonify(msg=" item is not complted")
  return jsonify(msg="invalid id,please enter valid id")
  

@app.route('/search',methods=['POST'])
def serch_todo():
  serch_item=request.json
  for i in datastore:
    if i['id']==serch_item['id']:
      return i
  return jsonify(msg="id was not found")
    
if __name__ =='__main__':
 app.run()  