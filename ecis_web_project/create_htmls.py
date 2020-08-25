import shutil
import fileinput

data = ["<nav aria-label=\"...\">\n\t<ul class=\"pagination pagination-sm\">\n\t\t<li class=\"page-item-disabled\">\n\t\t\t\t<span class=\"page-link\"><=</a>\n\t\t</li>\n"]
for i in range(48):
	data.append("\t\t<li class=\"page-item\"><a class=\"page-link\" href=\"{% url 'ecis_web_first_app:header"+str(i)+"' "+str(i*30+1)+" "+str((i+1)*30)+" %}\">"+str(i+1)+"</a></li>\n")
data.append("\t\t<li class=\"page-item\">\n\t\t\t<a class=\"page-link\" href=\"{% url 'ecis_web_first_app:header"+str(i)+"' 1370 1423 %}\">=></a>\n\t\t</li>\n\t</ul>\n</nav>")
for i in range(48):
	data2 =[]
	data2.extend(data)

	data2[i+1]="\t\t<li class=\"page-item active\" aria-current=\"page\"><span class=\"page-link\">"+str(i+1)+"<span class=\"sr-only\">(current)</span></span></li>\n"

	if i>0:
		data2[0]="<nav aria-label=\"...\">\n\t<ul class=\"pagination pagination-sm\">\n\t\t<li class=\"page-item\">\n\t\t\t\t<a class=\"page-link\" href=\"{% url 'ecis_web_first_app:header"+str(i-1)+"' "+str((i-1)*30+1)+" "+str(i*30)+" %}\" tabindex=\"-1\" aria-disabled=\"true\"><=</a>\n\t\t</li>\n"
	data2[49]="\t\t<li class=\"page-item\">\n\t\t\t<a class=\"page-link\" href=\"{% url 'ecis_web_first_app:header"+str(i+1)+"' "+str((i+1)*30+1)+" "+str((i+2)*30)+" %}\">=></a>\n\t\t</li>\n\t</ul>\n</nav>"

	shutil.copy2('ecis_web_first_app/templates/ecis_web_first_app/header.html', 'ecis_web_first_app/templates/ecis_web_first_app/new/header'+str(i)+'.html')
	rep_str = ""
	for item in data2:
		rep_str = rep_str+item
	for line in fileinput.FileInput('ecis_web_first_app/templates/ecis_web_first_app/new/header'+str(i)+'.html',inplace=1):
		if "TEXT_TO_SEARCH" in line:
			line=line.replace(line,rep_str)
		print(line, end='')
