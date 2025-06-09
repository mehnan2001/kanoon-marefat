from django.db.models import Q
from django.views import generic
from django.urls import reverse_lazy
from . import forms

from .models import CourseModel as Course

class AllCoursesView(generic.ListView):
    model = Course
    template_name = 'courses/course_list_view.html'
    context_object_name = 'courses'

    paginate_by = 6


    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            )

        return queryset

        # return Course.objects.all()


class CourseDetailView(generic.DetailView):
    template_name = 'courses/course_detail_view.html'
    model = Course
    context_object_name = 'course'


class CourseAddView(generic.CreateView):
    template_name = 'courses/add_edite_course.html'
    model = Course
    form_class = forms.CourseAddEditForm
    success_url = reverse_lazy('all_courses')  # Redirect to the list of courses after adding a new one

    def form_valid(self, form):
        # You can add custom logic here if needed
        return super().form_valid(form)


class CourseUpdateView(generic.UpdateView):
    template_name = 'courses/add_edite_course.html'
    model = Course

    form_class = forms.CourseAddEditForm
    success_url = reverse_lazy('all_courses')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_edit'] = True  # اضافه کردن وضعیت ویرایش
        return context

    def form_valid(self, form):
        return super().form_valid(form)


class CourseDeleteView(generic.DeleteView):
    model = Course
    template_name = 'courses/course_confirm_delete.html'  # صفحه تایید حذف
    success_url = reverse_lazy('all_courses')  # به کجا بره بعد از حذف موفق
