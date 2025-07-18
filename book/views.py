from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import RegisterForm,BookingForm
from django.contrib.auth import login
from django.shortcuts import render
from django.views.generic import TemplateView,ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from .forms import EmailLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from .models import Room,Booking

class Home(LoginRequiredMixin,TemplateView):
    print("Kanji")
    template_name = "admin/index.html"
    login_url = '/login/'  # optional: where to redirect if not logged in
    redirect_field_name = 'next'  # optional: default is 'next'

class Dashboard(TemplateView):
    template_name ="admin/index.html"

class Profile(TemplateView):
    template_name ="admin/users-profile.html"

class Contect(TemplateView):
    template_name = "admin/pages-contact.html"

class PageError(TemplateView):
    template_name =("admin/pages-error-404.html")

class BlankPage(TemplateView):
    template_name =("admin/pages-blank.html")

class MyForm(TemplateView):
    template_name=("admin/forms-layouts.html")

# class Login(TemplateView):
#     template_name=("admin/pages-login.html")

class ChartsApexcharts(TemplateView):
    template_name=("admin/charts-apexcharts.html")

class FormsLayouts(TemplateView):
    template_name=("admin/forms-layouts.html")

class PagesLogin(TemplateView):
    template_name=("admin/pages-login.html")

class PagesRegister(TemplateView):
    template_name=("admin/pages-register.html")

class ChartsChartjs(TemplateView):
    template_name=("admin/charts-chartjs.html")

class ChartsEcharts(TemplateView):
    template_name=("admin/charts-echarts.html")

class ComponentsAccordion(TemplateView):
    template_name=("admin/components-accordion.html")

class ComponentsAlerts(TemplateView):
    template_name=("admin/components-alerts.html")

class ComponentsBadges(TemplateView):
    template_name=("admin/components-badges.html")

class ComponentsBreadcrumbs(TemplateView):
    template_name=("admin/components-breadcrumbs.html")

class ComponentsButtons(TemplateView):
    template_name=("admin/components-buttons.html")

class ComponentsCards(TemplateView):
    template_name=("admin/components-cards.html")

class ComponentsCarousel(TemplateView):
    template_name=("admin/components-carousel.html")

class ComponentsListGroup(TemplateView):
    template_name=("admin/components-list-group.html")

class ComponentsModal(TemplateView):
    template_name=("admin/components-modal.html")

class ComponentsPagination(TemplateView):
    template_name=("admin/components-pagination.html")

class ComponentsProgress(TemplateView):
    template_name=("admin/components-progress.html")

class ComponentsSpinners(TemplateView):
    template_name=("admin/components-spinners.html")

class ComponentsTabs(TemplateView):
    template_name=("admin/components-tabs.html")

class ComponentsTooltips(TemplateView):
    template_name=("admin/components-tooltips.html")

class FormsEditors(TemplateView):
    template_name=("admin/forms-editors.html")

class FormsElements(TemplateView):
    template_name=("admin/forms-elements.html")

class FormsValidation(TemplateView):
    template_name=("admin/forms-validation.html")

class IconsBootstrap(TemplateView):
    template_name=("admim/icons-bootstrap.html")

class IconsBoxicons(TemplateView):
    template_name=("admin/icons-boxicons.html")

class IconsRemix(TemplateView):
    template_name=("admin/icons-remix.html")

class PagesBlank(TemplateView):
    template_name=("admin/pages-blank.html")

class PagesFaq(TemplateView):
    template_name=("admin/pages-faq.html")

class PagesRegister(TemplateView):
    template_name=("admin/pages-register.html")

class TablesData(TemplateView):
    template_name=("admin/tables-data.html")

class TablesGeneral(TemplateView):
    template_name=("admin/tables-general.html")

class UsersProfile(TemplateView):
    template_name=("users-profile.html")

class CustomLoginView(LoginView):
    form_class = EmailLoginForm
    template_name=("admin/pages-login.html")
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('account:home'))  # Change to your home URL name/path
        return super().dispatch(request, *args, **kwargs)


    def form_valid(self, form):
        login(self.request, form.get_user())
        return redirect(reverse_lazy('account:home'))  # Update this
    

class RegisterView(FormView):
    template_name=("admin/pages-register.html")
    form_class = RegisterForm
    success_url = reverse_lazy('account:home') 
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('account:home'))  # Change to your home URL name/path
        return super().dispatch(request, *args, **kwargs)
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

class SecureLogoutView(LogoutView):
    http_method_names = ['post']  # restrict to POST only
    next_page = '/'


# CRUD of Room
class RoomListView(LoginRequiredMixin, ListView):
    model = Room
    template_name = 'admin/tables-data.html'
    context_object_name = 'rooms'


class RoomDetailView(LoginRequiredMixin, DetailView):
    model = Room
    template_name = 'admin/rooms/room_detail.html'
    context_object_name = 'room'


class RoomCreateView(LoginRequiredMixin, CreateView):
    model = Room
    fields = ['room_number', 'room_type', 'price_per_night', 'is_available', 'capacity']
    template_name = 'admin/rooms/room_form.html'
    success_url = reverse_lazy('account:room_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class RoomUpdateView(LoginRequiredMixin, UpdateView):
    model = Room
    fields = ['room_number', 'room_type', 'price_per_night', 'is_available', 'capacity']
    template_name = 'admin/rooms/room_form.html'
    success_url = reverse_lazy('account:room_list')

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class RoomDeleteView(LoginRequiredMixin, DeleteView):
    model = Room
    template_name = 'admin/rooms/room_confirm_delete.html'
    success_url = reverse_lazy('account:room_list')



class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'admin/bookings/booking_list.html'
    context_object_name = 'bookings'

class BookingDetailView(LoginRequiredMixin, DetailView):
    model = Booking
    template_name = 'admin/bookings/booking_detail.html'
    context_object_name = 'booking'

class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'admin/bookings/booking_form.html'
    success_url = reverse_lazy('account:booking_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)

class BookingUpdateView(LoginRequiredMixin, UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = 'admin/bookings/booking_form.html'
    success_url = reverse_lazy('account:booking_list')

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)

class BookingDeleteView(LoginRequiredMixin, DeleteView):
    model = Booking
    template_name = 'admin/bookings/booking_confirm_delete.html'
    success_url = reverse_lazy('account:booking_list')

