from django.shortcuts import render
from django.contrib import messages
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, ListView, TemplateView

from .models import *


# Create your views here.

class DashboardView(TemplateView):
	template_name = 'dashboard_home.html'


class CategoryActionMixin(object):

	fields = ['name', 'slug', 'image']

	@property
	def success_msg(self):
		return NotImplemented

	def form_valid(self, form):
		messages.info(self.request, self.success_msg)
		return super(CategoryActionMixin, self).form_valid(form)



class SubCategoryActionMixin(object):

	fields = ['name', 'description', 'parent_category', 'suppliers']

class SupplierActionMixin(object):

	fields = ['name', 'description', 'website', 'logo']

class CategoryDetailView(DetailView):

	model = Category

	template_name = 'category_detail.html'

class CategoryListView(ListView):

	model = Category
	context_object_name = 'category_list'
	template_name = 'category_list.html'

	def get_queryset(self):

		print 'test'
		return Category.objects.all()

class CategoryCreateView(CategoryActionMixin, CreateView):

	model = Category

	#template_name = 'edit_category.html'
	template_name = 'category_edit.html'

	'''def get_succes_url(self):

		return '''

class CategoryUpdateView(CategoryActionMixin, UpdateView):

	model = Category
	fields = ['name', 'image', 'slug']

	#template_name = 'edit_category.html'
	template_name = 'category_edit.html'



class CategoryDeleteView(DeleteView):

	model = Category
	success_url = 'www.google.be'

	template_name = 'delete_category.html'


class SubCategoryDetailView(DetailView):

	model = SubCategory

class SubCategoryListView(ListView):

	model = SubCategory

class SubCategoryCreateView(SubCategoryActionMixin, CreateView):

	model = SubCategory

	template_name = 'subcategory_edit.html'


class SupplierCreateView(SupplierActionMixin, CreateView):

	model = Supplier

	template_name = 'supplier_edit.html'

class SupplierUpdateView(SupplierActionMixin, UpdateView):

	model = Category

	template_name = 'supplier_edit.html'
