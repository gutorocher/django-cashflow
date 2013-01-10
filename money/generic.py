from django.views.generic.list import ListView
from django.views.generic.edit import ModelFormMixin, ProcessFormView

class ModelFormWithListView(ListView, ModelFormMixin, ProcessFormView):

	def post(self, request, *args, **kwargs):
		try:
			self.object = self.get_object()
		except:
			self.object = None
		return super(ModelFormWithListView, self).post(request, *args, **kwargs)

	def get_context_data(self, **kwargs):

		self.object_list = self.get_queryset()

		try:
			self.object = self.get_object()
		except:
			self.object = None

		kwargs.update({
			'object_list' : self.object_list,
			'form' : self.get_form(self.get_form_class()),
			'object' : self.object
		})

		return super(ModelFormWithListView, self).get_context_data(**kwargs)
