'''
Realice pruebas unitarias al modelo Laboratorio, donde se verifique: 
1.- Que los datos en nuestra base de datos simulada coincidan con los que se crearon inicialmente 
en setUpTestData para un laboratorio dado.  

2.-La URL para confirmar que devuelve una respuesta HTTP 200 para laboratorio. 

3.- Y finalmente, que la página usando reverse para llamar al nombre de la URL, busca una 
respuesta HTTP 200, verifica que se use la plantilla correcta, y confirma que el contenido HTML 
coincide con lo esperado. 

'''
from django.test import TestCase
from django.urls import reverse
from .models import Laboratorio

class LaboratorioModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Laboratorio.objects.create(nombre='Laboratorio A', ciudad='Santiago', pais='Chile')

    def test_nombre_laboratorio(self):
        laboratorio = Laboratorio.objects.get(id=1)
        self.assertEqual(laboratorio.nombre, 'Laboratorio A')

    def test_ciudad_laboratorio(self):
        laboratorio = Laboratorio.objects.get(id=1)
        self.assertEqual(laboratorio.ciudad, 'Santiago')

    def test_pais_laboratorio(self):
        laboratorio = Laboratorio.objects.get(id=1)
        self.assertEqual(laboratorio.pais, 'Chile')


class LaboratorioURLTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Laboratorio.objects.create(nombre='Laboratorio B', ciudad='Valparaíso', pais='Chile')

    def test_url_accesible_por_nombre(self):
        response = self.client.get(reverse('laboratorio:editar', args=[2]))
        self.assertEqual(response.status_code, 200)

    def test_url_existe_en_ubicacion_deseada(self):
        response = self.client.get('/laboratorio/editar/2/')
        self.assertEqual(response.status_code, 200)


class LaboratorioVistaTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Laboratorio.objects.create(nombre='Laboratorio C', ciudad='Concepción', pais='Chile')

    def test_vista_usa_plantilla_correcta(self):
        response = self.client.get(reverse('laboratorio:editar', args=[3]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'laboratorio/crear_laboratorio.html')

    def test_vista_contiene_html_correcto(self):
        response = self.client.get(reverse('laboratorio:editar', args=[3]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<form method="post">')
