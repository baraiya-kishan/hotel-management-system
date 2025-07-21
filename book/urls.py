from django.urls import path
from book.views import *
from django.contrib.auth.views import LogoutView


# from u
app_name="account"
urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('dashboard/',Dashboard.as_view(),name='dashboard'),
    path('my-profile/',Profile.as_view(),name='profile'),
    # path('login/',Login.as_view(),name='login'),
    path('contact/',Contect.as_view(),name='contact'),
    path('pageerror',PageError.as_view(),name='pageerroe'),
    path('blankpage',BlankPage.as_view(),name='blankpage'),
    path("charts-apexcharts/", ChartsApexcharts.as_view(), name="charts_apexcharts"),
    path("forms-layouts/", FormsLayouts.as_view(), name="forms_layouts"),
    path("pages-login/", PagesLogin.as_view(), name="pages_login"),
    path("pages-register/", PagesRegister.as_view(), name="pages_register"),
    path("charts-chartjs/", ChartsChartjs.as_view(),name="charts_chartjs"),
    path("charts-echarts/",ChartsEcharts .as_view(), name="charts_echarts"),
    path("components-accordion/",ComponentsAccordion.as_view(),name="components_accordion"),
    path("components-alerts/",ComponentsAlerts.as_view(),name="components_alerts"),
    path("components-badges/",ComponentsBadges.as_view(),name="components_badges"),
    path("components-breadcrumbs/", ComponentsBreadcrumbs.as_view(), name="components_breadcrumbs"),
    path("components-buttons/", ComponentsButtons.as_view(), name="components_buttons"),
    path("components-cards/",ComponentsCards.as_view(), name="components_cards"),
    path("components-carousel/",ComponentsCarousel .as_view(), name="components_carousel"),
    path("components-list-group/", ComponentsListGroup.as_view(), name="components_list_group"),
    path("components-modal/",ComponentsModal .as_view(), name="components_modal"),
    path("components-pagination/",ComponentsPagination .as_view(), name="components_pagination"),
    path("components-progress/", ComponentsProgress.as_view(), name="components_progress"),
    path("components-spinners/", ComponentsSpinners.as_view(), name="components_spinners"),
    path("components-tabs/",ComponentsTabs .as_view(), name="components_tabs"),
    path("components-tooltips/", ComponentsTooltips.as_view(), name="components_tooltips"),
    path("forms-editors/", FormsEditors.as_view(), name="forms_editors"),
    path("forms-elements/", FormsElements.as_view(), name="forms_elements"),
    path("forms-validation/", FormsValidation.as_view(), name="forms_validation"),
    path("icons-bootstrap/",IconsBootstrap .as_view(), name="icons_bootstrap"),
    path("icons-boxicons/", IconsBoxicons.as_view(), name="icons_boxicons"),
    path("icons-remix/", IconsRemix.as_view(), name="icons_remix"),
    path("pages-blank/", PagesBlank.as_view(), name="pages_blank"),
    path("pages-faq/", PagesFaq.as_view(), name="pages_faq"),
    # path("pages-register/", PagesRegister.as_view(), name="pages_register"),
    path("tables-data/", TablesData.as_view(), name="tables_data"),
    path("tables-general/", TablesGeneral.as_view(), name="tables_general"),
    path("users-profile/", UsersProfile.as_view(), name="users_profile"),

    # custome login and reg
    path('login/', CustomLoginView.as_view(), name='pages_login'),
    path('register/', RegisterView.as_view(), name='pages_register'),
    path('logout/', SecureLogoutView.as_view(), name='logout'),

    # crud urls for room
    path('room/', RoomListView.as_view(), name='room_list'),
    path('room/add/', RoomCreateView.as_view(), name='room_create'),
    path('room/<int:pk>/', RoomDetailView.as_view(), name='room_detail'),
    path('room/<int:pk>/edit/', RoomUpdateView.as_view(), name='room_update'),
    path('room/<int:pk>/delete/', RoomDeleteView.as_view(), name='room_delete'),
    #crud urls for booking
    path('bookings/', BookingListView.as_view(), name='booking_list'),
    path('booking/add/', BookingCreateView.as_view(), name='booking_create'),
    path('booking/<int:pk>/', BookingDetailView.as_view(), name='booking_detail'),
    path('booking/<int:pk>/edit/', BookingUpdateView.as_view(), name='booking_update'),
    path('booking/<int:pk>/delete/', BookingDeleteView.as_view(), name='booking_delete'),
#add paths
]
 