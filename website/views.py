from django.shortcuts import render
from rest_framework import generics,permissions

from .serializers import TeamSerializer,PlayerSerializer,UserSerializer
from .models import Team,Player
from .forms import TeamForm,UserForm,PlayerForm
from django.contrib.auth.models import User
from django.views.generic import TemplateView
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http import HttpResponseBadRequest,HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth import authenticate, login, logout
# Create your views here.

class UserList(generics.ListCreateAPIView):
	model = User
	serializer_class = UserSerializer
	queryset = User.objects.all()

class UserDetail(generics.RetrieveAPIView):
	model = User
	serializer_class = UserSerializer
	queryset = User.objects.all()

class PlayerList(generics.ListCreateAPIView):
	model = Player
	serializer_class = PlayerSerializer
	queryset = Player.objects.all()

class PlayerDetail(generics.RetrieveAPIView):
	model = Player
	serializer_class = PlayerSerializer
	queryset = Player.objects.all()
	

class TeamList(generics.ListCreateAPIView):
	model = Team
	serializer_class = TeamSerializer
	queryset = Team.objects.all()

	def get(self,request,format=None):
		# print(request.GET)
		# print(request.GET['teamList'])

		if request.user.is_authenticated() and 'onlyOneTeam' in request.GET:
			team = Team.objects.get(manager=request.user)
			team = TeamSerializer(team).data
		elif request.user.is_authenticated() == 0 or 'onlyOneTeam' not in request.GET:
			team = Team.objects.all()
			team = TeamSerializer(team, many=True).data
		

		# team = Team.objects.get(manager=request.user)

		
		return Response(team)

class TeamDetail(generics.RetrieveAPIView):
	model = Team
	serializer_class = TeamSerializer
	queryset = Team.objects.all()


########################### HOME VIEW ###########################
def home_view(request):
    return render(request,'base.html')
########################### END VIEW ########################### 

def create_team(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()

    return render(request, 'home.html', {'form': form})


class UserFormView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super(UserFormView, self).get_context_data(**kwargs)
        context.update(form=UserForm())
        return context

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(UserFormView, self).dispatch(*args, **kwargs)

@csrf_exempt
def signup(request):
        in_data = json.loads(str(request.body, 'utf-8'))
        # bound_contact_form = CheckoutForm(data={'username': in_data.get('username'),
        # 										'email': in_data.get('email'),
        # 										'password': in_data.get('password')})
        # now validate ‘bound_contact_form’ and use it as in normal Django
        print(in_data)
        username_data = in_data['username']
        password_data = in_data['password']
        user_obj = User.objects.create_user(username=username_data,email=in_data['email'],password=password_data)

        print(user_obj)
        print(username_data)
        user_obj.save()

        user = authenticate(username=username_data, password=password_data)
        if user is not None:
            login(request, user)
            print("Logou")
            userLogedIn = UserSerializer(request.user).data
            return Response(userLogedIn)
        else:
        	return HttpResponse('Login error', status=401)


@csrf_exempt
def createTeam(request):
        in_data = json.loads(str(request.body, 'utf-8'))
        # bound_contact_form = CheckoutForm(data={'username': in_data.get('username'),
        # 										'email': in_data.get('email'),
        # 										'password': in_data.get('password')})
        # now validate ‘bound_contact_form’ and use it as in normal Django
        print(in_data)
        name_data = in_data['name']
        manager = request.user
        print(manager)
        team_obj = Team(name=name_data,manager=manager)

        team_obj.save()


def createPlayer(request):
        in_data = json.loads(str(request.body, 'utf-8'))

        print(in_data)
        name_data = in_data['name']
        position_data = in_data['position']
        country_data = in_data['country']
        realLife_team = in_data['realLifeTeam']

        team = Team.objects.get(manager=request.user)
        print(team)
        player_obj = Player(name=name_data,position=position_data,country=country_data,realLife_team=realLife_team, team=team)
        print(player_obj)
        player_obj.save()
        return HttpResponse(status=200)

@api_view(('GET', 'POST'))
def updatePlayer(request):
    # in_data = json.loads(str(request.body, 'utf-8'))
    in_data = request.data
    # if 'player_id' in request.POST:
    print(in_data)
    player_id = int(in_data['player_id'])
    print(player_id)
    Player.objects.filter(id=player_id).update(
        name = in_data['nameUpdated'],
        position = in_data['positionUpdated'],
        country = in_data['countryUpdated'],
        realLife_team = in_data['realLifeTeamUpdated']
    )

    player = Player.objects.get(id=player_id)
    player = PlayerSerializer(player).data
    print(player)

    return Response(player)



#PARA PODER MANDAR UM RESPONSE() COM O USER SE FOSSE USAR UMA VIEW NORMAL NAO FUNCIONARIA, DARIA ESSE ERRO: .accepted_renderer not set on Response
#PQ O RESPONSE SO FUNCIONA COM .accepted_renderer que eh The renderer instance that will be used to render the response. e eh APIView or @api_view
#E TEM QUE SERIALIZAR PQ NAO DA PRA MANDAR OBJETOS NO RESPONSE
#The renderers used by the Response class cannot natively handle complex datatypes such as Django model instances,
#so you need to serialize the data into primitive datatypes before creating the Response object.
@csrf_exempt
@api_view(('GET', 'POST'))
def logIn(request):
        # in_data = json.loads(str(request.body, 'utf-8'))
        in_data = request.data
        # TAVA DANDO ESSE ERRO PQ POR ALGUM MOTIVO QUANDO ELE TAVA NO MIDDLEWARE process_request or process_view ELE ACESSAVA O request.POST
        # AI POR ISSO NAO PODIA MAIS ACESSAR O BODY DA REQUEST NA VIEW, DAVA ERRO EM request.body
        # Exception: You cannot access body after reading from request's data stream
        # ENTAO PRA RESOLVER TEM COMO:
        # If you are using django-rest-framework, then you can just use request.data instead of trying to parse json from the request yourself
        # USAR resquest.data do request modificado do DRF pq REST framework's Request class extends the standard HttpRequest
        print(in_data)
        username_data = in_data['username']
        password_data = in_data['password']

        print(username_data)
        user = authenticate(username=username_data, password=password_data)
        if user is not None:
            login(request, user)
            print("Logou")
            userLogedIn = UserSerializer(request.user).data
            return Response(userLogedIn)
        else:
        	return HttpResponse('Login error', status=401)



def logOut(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    return HttpResponse(status=200)

def getTeam(request):

	team = Team.objects.get(manager=request.user)
	print(team)

	return team

@api_view(('GET', 'POST'))
def getUser(request):

    userLogedIn = UserSerializer(request.user).data
    return Response(userLogedIn)

@api_view(('GET', 'POST'))
def getPlayers(request):

    players = Player.objects.filter(team__manager=request.user)
    print(players)
    players = PlayerSerializer(players, many=True).data
    return Response(players)


		
