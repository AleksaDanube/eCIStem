import shutil
f = open("view_funcs.txt", "a")
c = open("urls_funcs.txt", "a")
for i in range(47):
	f.write("def header"+str(i)+"(request, min, max):\n")
	f.write("\topids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)\n")
	f.write("\toperons_dict = {'operons_list':opids}\n")
	f.write("\treturn render(request, 'ecis_web_first_app/header"+str(i)+".html', operons_dict)\n")
	c.write("\tpath(r'^header"+str(i)+"/<str:min>/<str:max>/', views.header"+str(i)+", name = 'header"+str(i)+"'),\n")
f.close()
c.close()

#opids = Operons.objects.all().values('operon_ID')
#for item in opids:
# 	print(str(item['operon_ID']))
# 	#shutil.copy2('ecis_web_first_app/templates/ecis_web_first_app/operon1158.html', 'ecis_web_first_app/templates/ecis_web_first_app/new/operon'+item['operon_ID']+'.html')
# 	f = open("view_funcs.txt", "a")
# 	f.write("def operon"+str(item['operon_ID'])+"(request):\n")
# 	f.write("\topid = Operons.objects.get(operon_ID__exact="+str(item['operon_ID'])+")\n")
# 	f.write("\tgenes = EcisDataBase.objects.filter(operon_ID="+str(item['operon_ID'])+")\n")
# 	f.write("\tspecies = Species.objects.get(genome_ID_x=genes[0]['genome_ID_x'])\n")
# 	f.write("\tclust_dict = {\"genes_list\": genes, \"species_list\":species, \"opid\":opid}\n")
# 	f.write("\treturn render(request, 'ecis_web_first_app/operon"+str(item['operon_ID'])+".html', clust_dict)\n")
# 	f.close()
	# f = open("urls_funcs.txt", "a")
	# f.write("\turl(r'^operon"+str(item['operon_ID'])+"/', views.operon"+str(item['operon_ID'])+", name='operon"+str(item['operon_ID'])+"')]\n")


# clsts = Clust40PG.objects.all().values('clust40pg')
# for item in clsts:
# 	print(str(item['clust40pg']))
#	shutil.copy2('ecis_web_first_app/templates/ecis_web_first_app/Cluster%2033.html', 'ecis_web_first_app/templates/ecis_web_first_app/new/'+str(item['clust40pg']).replace(" ", "%20")+'.html')
# 	f = open("view_funcs_clusts.txt", "a")
# 	f.write("def "+str(item['clust40pg']).replace(" ","")+"(request):\n")
# 	f.write("\tclst = Clust40PG.objects.get(clust40pg__exact=\""+str(item['clust40pg'])+"\")\n")
# 	f.write("\tgenes = EcisDataBase.objects.filter(clust40pg__exact=\""+str(item['clust40pg'])+"\")\n")
# 	f.write("\tclust_dict = {\"genes_list_within_clust\": genes, \"clst40\":clst}\n")
# 	f.write("\treturn render(request, 'ecis_web_first_app/"+str(item['clust40pg']).replace(" ", "%20")+".html', clust_dict)\n")
# 	f.close()

# 	f = open("urls_funcs_clusters.txt", "a")
# 	f.write("\turl(r'^"+str(item['clust40pg'])+"/', views."+str(item['clust40pg']).replace(" ", "")+", name="+str(item['clust40pg']).replace(" ","%20")+"')\n")
