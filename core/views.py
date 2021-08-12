from django.shortcuts import render
from core.models import Evento
# Create your views here.

# funcao para redirecionar a aplicação para outra pagina
#    def index(request):
#        return redirect('/admin/')
# fim da funao

def lista_eventos(request):
    # usuario = request.user
    evento = Evento.objects.all()
    dados = {'eventos':evento}
    return render(request,'agenda.html', dados)
