from django.contrib import admin

from .models import Preguntas, ElegirRespuesta
from .forms import ElegirInlineFormset
from apps.resultados.models import PreguntasRespondidas

class ElegirRespuestaInline(admin.TabularInline):
	model = ElegirRespuesta
	can_delete = False
	max_num = ElegirRespuesta.MAXIMO_RESPUESTA
	min_num = ElegirRespuesta.MAXIMO_RESPUESTA
	formset = ElegirInlineFormset
class PreguntasAdmin(admin.ModelAdmin):
	model = Preguntas
	inlines = (ElegirRespuestaInline, )
	list_display = ['consigna',]
	search_fields = ['consigna', 'preguntas__texto']

class PreguntasRespondidasAdmin(admin.ModelAdmin):
	list_display = ['preguntas', 'respuesta', 'correcta', 'puntaje_obtenido']

	class Meta:
		model =PreguntasRespondidas


admin.site.register(PreguntasRespondidas)
admin.site.register(Preguntas, PreguntasAdmin)
admin.site.register(ElegirRespuesta)

# Register your models here.
