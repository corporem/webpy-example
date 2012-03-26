'''
Created on Mar 24, 2012

@author: sotuzun
'''
import settings
import web

urls = (
	'/', 'Index'
)

app = web.application(urls, globals())

render = web.template.render(settings.TEMPLATE_FOLDER, base=settings.BASE_TEMPLATE_NAME)

class Index:
	
	def GET(self):
		return render.index()
	
	def POST(self):
		try:
			data = web.input(op1=0, op2=0);
			sum_tot = int(data.op1) + int(data.op2)
			return render.result(data.op1, data.op2, sum_tot)
		except:
			raise web.seeother('/')

if __name__ == '__main__':
	app.run()
