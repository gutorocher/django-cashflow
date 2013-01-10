from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required

class RestrictedListView(generic.ListView):
    ''' Generic list view that checks permissions '''
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        @permission_required('%s.change_%s' % (self.model._meta.app_label, self.model._meta.module_name))
        def wrapper(request, *args, **kwargs):
            return super(RestrictedListView, self).dispatch(request, *args, **kwargs)
        return wrapper(request, *args, **kwargs)

class RestrictedUpdateView(generic.UpdateView):
    ''' Generic update view that checks permissions '''
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        @permission_required('%s.change_%s' % (self.model._meta.app_label, self.model._meta.module_name))
        def wrapper(request, *args, **kwargs):
            return super(RestrictedUpdateView, self).dispatch(request, *args, **kwargs)
        return wrapper(request, *args, **kwargs)

class RestrictedCreateView(generic.CreateView):
    ''' Generic create view that checks permissions '''
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        @permission_required('%s.add_%s' % (self.model._meta.app_label, self.model._meta.module_name))
        def wrapper(request, *args, **kwargs):
            return super(RestrictedCreateView, self).dispatch(request, *args, **kwargs)
        return wrapper(request, *args, **kwargs)

class RestrictedDeleteView(generic.DeleteView):
    ''' Generic delete view that checks permissions '''
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        @permission_required('%s.delete_%s' % (self.model._meta.app_label, self.model._meta.module_name))
        def wrapper(request, *args, **kwargs):
            return super(RestrictedDeleteView, self).dispatch(request, *args, **kwargs)
        return wrapper(request, *args, **kwargs)

class LoginRequired(generic.View):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequired, self).dispatch(request, *args, **kwargs)

class ModelFormWithListView(RestrictedListView, generic.edit.ModelFormMixin, generic.edit.ProcessFormView):

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
