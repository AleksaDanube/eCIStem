from django.shortcuts import render
from django.http import HttpResponse
from .models import Clust40PG,Operons,Species,EcisDataBase,PfamDb
from django.core.paginator import Paginator
from PIL import Image
import shutil
from django.db.models.functions import Lower
# Create your views here.
def homepage(request):
	phylums_list = []
	phylums = Species.objects.all()
	pfams = PfamDb.objects.order_by(Lower('pfam_name').asc())

	pfams_list = pfams.values_list('pfam_name',flat=True)
	#print(pfams_list)
	#phylums_dict = {'phylum_list':phylums}
	#print(list(phylums))
	phylums_list = phylums.values_list('phylum',flat=True)
	#phylum_values = phylums.values('phylum')
	#print(phylum_values)
	#for item in phylum_values:
		#print(item)
		#phylums_list.append(item['phylum'])
	#print(set(phylums_list))
	# for item in genoms:
	# 	opid.extend(Operons.objects.filter(operon_ID__exact=item.operon_ID))
	#
	# #print(opid)
	print(set(pfams_list))
	phylums_dict = {"phylums_list":sorted(set(phylums_list)), "pfams_list":sorted(set(pfams_list))}
	return render(request, 'ecis_web_first_app/homepage.html', phylums_dict)
def header0(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	genome_ids = opids.values_list('genome_ID_x')
	org_list = Species.objects.filter(genome_ID_x__in=genome_ids)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header0.html', operons_dict)
def header1(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header1.html', operons_dict)
def header2(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header2.html', operons_dict)
def header3(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header3.html', operons_dict)
def header4(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header4.html', operons_dict)
def header5(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header5.html', operons_dict)
def header6(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header6.html', operons_dict)
def header7(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header7.html', operons_dict)
def header8(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header8.html', operons_dict)
def header9(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header9.html', operons_dict)
def header10(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header10.html', operons_dict)
def header11(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header11.html', operons_dict)
def header12(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header12.html', operons_dict)
def header13(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header13.html', operons_dict)
def header14(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header14.html', operons_dict)
def header15(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header15.html', operons_dict)
def header16(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header16.html', operons_dict)
def header17(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header17.html', operons_dict)
def header18(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header18.html', operons_dict)
def header19(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header19.html', operons_dict)
def header20(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header20.html', operons_dict)
def header21(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header21.html', operons_dict)
def header22(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header22.html', operons_dict)
def header23(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header23.html', operons_dict)
def header24(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header24.html', operons_dict)
def header25(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header25.html', operons_dict)
def header26(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header26.html', operons_dict)
def header27(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header27.html', operons_dict)
def header28(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header28.html', operons_dict)
def header29(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header29.html', operons_dict)
def header30(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header30.html', operons_dict)
def header31(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header31.html', operons_dict)
def header32(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header32.html', operons_dict)
def header33(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header33.html', operons_dict)
def header34(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header34.html', operons_dict)
def header35(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header35.html', operons_dict)
def header36(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header36.html', operons_dict)
def header37(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header37.html', operons_dict)
def header38(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header38.html', operons_dict)
def header39(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header39.html', operons_dict)
def header40(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header40.html', operons_dict)
def header41(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header41.html', operons_dict)
def header42(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header42.html', operons_dict)
def header43(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header43.html', operons_dict)
def header44(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header44.html', operons_dict)
def header45(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header45.html', operons_dict)
def header46(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	operons_dict = {'operons_list':opids}
	return render(request, 'ecis_web_first_app/header46.html', operons_dict)
def header47(request, min, max):
	opids = Operons.objects.filter(index_ID__gte=min, index_ID__lte=max)
	#--try to match operons and phylums tbd
	genes = EcisDataBase.objects.filter(operon_ID__in=opids.values_list('operon_ID',flat=True))
	phyls = Species.objects.filter(genome_ID_x__in = genes.values_list('genome_ID_x',flat=True))
	#operons_phylums_dict = zip(genes.operon_ID,phyls.phylum)
	#----------------------------------
	operons_dict = {'operons_list':opids}
	print(operons_dict,phyls)
	return render(request, 'ecis_web_first_app/header47.html', operons_dict)
def pfams_det(request, gene):
	pfams = []
	pfams = PfamDb.objects.filter(gene_id__exact=gene)
	print(pfams.values('genome_ID'))

	pfams_dict = {"pfam_list":pfams,"gene_id":gene}
	return render(request,'ecis_web_first_app/pfams_det.html',pfams_dict)

def PhylumSearch(request, phylum_name):
	phyls = Species.objects.filter(phylum__exact = phylum_name)
	gmid_values = phyls.values('genome_ID_x')
	genoms = EcisDataBase.objects.filter(genome_ID_x__in=gmid_values)
	opid_list =list(set(genoms.values_list('operon_ID',flat=True)))
	operons_list = Operons.objects.filter(operon_ID__in = opid_list)
	paginator = Paginator(operons_list, 25) # Show 25 contacts per page.
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request, 'ecis_web_first_app/phylumsearch.html',  {"phyls_list":phyls[0],'page_obj': page_obj})

def pfamsearch(request, pfam_name_id):
	pfams = PfamDb.objects.filter(pfam_name__exact = pfam_name_id)
	gene_values = pfams.values('gene_id')
	genes = EcisDataBase.objects.filter(gene_id__in=gene_values)
	opid_list =list(set(genes.values_list('operon_ID',flat=True)))
	operons_list = Operons.objects.filter(operon_ID__in = opid_list)
	paginator = Paginator(operons_list, 25) # Show 25 contacts per page.
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request, 'ecis_web_first_app/pfamsearch.html',  {"pfams_list":pfams[0],'page_obj': page_obj})
def core_det(request, core_whole_id):
	genes = EcisDataBase.objects.filter(core_whole__exact=core_whole_id)
	paginator = Paginator(genes, 50) # Show 25 contacts per page.
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	genes_dict = {"genes_list_within_core_whole_id": genes, "core":core_whole_id, 'page_obj': page_obj}
	return render(request, 'ecis_web_first_app/core_det.html', genes_dict)
def operonsearch(request):
	search_term = request.GET.get('q')
	print('search_term is ' +search_term)
	try:
		operons = Operons.objects.get(operon_ID = search_term)
		ops_dict = {"operon_list":operons}
	except Operons.DoesNotExist:
		ops_dict = {"operon_list":[]}


	return render(request, 'ecis_web_first_app/operonsearch.html', ops_dict)
def genusearch(request):
	search_term = request.GET.get('q')
	print('search_term is ' +search_term)
	try:
		operons = Operons.objects.filter(genus__exact = search_term)
		ops_dict = {"operon_list":operons, "sp":search_term}

	except Operons.DoesNotExist:
		ops_dict = {"operon_list":[]}


	return render(request, 'ecis_web_first_app/genusearch.html', ops_dict)

def operon_det(request, operon_id):
	search_term = ''
	opid = ''
	genes = ''
	species = ''
	pfams = {}
	opid = Operons.objects.get(operon_ID__exact=operon_id)
	genes = EcisDataBase.objects.filter(operon_ID=operon_id)
	genes_values = genes.values('genome_ID_x')
	scaffold = genes.values('scaffold')[0]
	scaffold['scaffold'] = scaffold['scaffold'].replace('_', ' ')
	species = Species.objects.get(genome_ID_x=genes_values[0]['genome_ID_x'])
	#print(EcisDataBase.objects.filter(genome_ID_x__exact=str(genes.values('genome_ID_x')).values('operon_ID')))
	#gene_ids = genes.values('gene_id')
	# for item in genes.values_list('gene_id',flat=True):
	# 	pfams[item] =  PfamDb.objects.filter(gene_id__exact = item).values('pfam_name')
	# print(pfams)
	#pfams = PfamDb.objects.filter(gene_id__in=genes.values_list('gene_id',flat=True))
	operon_dict = {"genes_list": genes, "species_list": species, "opid":opid, "scaffold":scaffold }
	return render(request, 'ecis_web_first_app/operon_det.html', operon_dict)

def cluster_det(request, cluster_id):
	print('clust is ' + cluster_id)
	clst = Clust40PG.objects.get(clust40pg__exact=cluster_id)
	genes = EcisDataBase.objects.filter(clust40pg__exact=cluster_id)
	clust_dict = {"genes_list_within_clust": genes, "clst40":clst}
	return render(request, 'ecis_web_first_app/cluster_det.html', clust_dict)
