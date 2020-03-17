class Field(object):
	def __init__(self,name,column_type):
		self.name=name
		self.column_type=column_type
	def __str__(self):
		return '<%s:%s>'%(self.name,self.column_type)


class StringField(Field):
	def __init__(self,name):
		super(StringField,self).__init__(name,'varchar(100)')



class IntegerField(Field):
	def __init__(self,name):
		super(IntegerField,self).__init__(name,'bigint')



class ModelMetaclass(type):
	def __new__(cla,name,bases,attrs):
		if name=='Model':
			return type.__new__(cla,name,bases,attrs)
		print('Found model:%s'%name)
		mappings=dict()
		for k,v in attrs.items():
			if isinstance(v,Field):
				print('Found mappings:%s==>%s:%s'%(k,v.name,v.column_type))
				mappings[k]=v
		for k in mappings.keys():
			attrs.pop(k)
		attrs['__mappings__']=mappings
		attrs['__table__']=name
		return type.__new__(cla,name,bases,attrs)




class Model(dict,metaclass=ModelMetaclass):
	def __init__(self,**kw):
		super(Model,self).__init__(**kw)
	def __getattr__(self,key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Model' object has no attribute '%s'"%key)
	def __setattr__(self,key,value):
		self[key]=value
	def save(self):
		fields=[]
		params=[]
		args=[]
		type_=[]
		NAME=[]
		for k,v in self.__mappings__.items():
			fields.append(v.name)
			params.append(str(self[k]))
			args.append(str(self[k]))
			type_.append(v.column_type)
			NAME.append(k)
		sql='insert into %s (%s) values (%s)'%(self.__table__,','.join(fields),','.join(params))
		print('SQL:%s'%sql)
		print('ARGS:(%s)(%s)(%s)'%(NAME,args,type_))


class User(Model):
	id=IntegerField('id')
	name=StringField('username')
	email=StringField('email')
	password=StringField('password')



u=User(id=12345,name='cao',email='1225060015@qq.com',password='1234567')
u.save()
