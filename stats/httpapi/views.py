import os.path
import datetime
import json
import csv
import io
import socket
from stats.httpapi.models import Acter, Film, Stats
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
#from django.http import HttpResponse
#from wsgiref.util import FileWrapper
from rest_framework.views import APIView
from rest_framework import status
from django.db.models import Count, Max, Min
from django.core import serializers

class FilmAPI(APIView):
    parser_classes = (FileUploadParser,)


class MoviesPut(FilmAPI):
    def put(self, request, filename, format=None):
        data = {}
        acters = {}
        try:
            Stats.objects.all().delete()
            Film.objects.all().delete()
            Acter.objects.all().delete()

            up_file = request.FILES['file']
            data = json.loads(up_file.read().decode())
            
            for film in data['films']:
                f = Film.objects.create(title=film['title'], description=film['description'])
                for acter in film['acters']:
                    if acter not in acters.keys():
                        acters[acter] = Acter.objects.create(name=acter)
                    f.acters.add(acters[acter])


            return Response(data, status.HTTP_200_OK)
        except Exception as error:
            print(error)
            return Response(status.HTTP_404_NOT_FOUND)

    def post(self, request, filename, format=None):
        return self.put(request, filename, format)


class StatsPut(FilmAPI):
    def put(self, request, filename, format=None):
        res = {}
        try:
            up_file = request.FILES['file']
            data = csv.DictReader(io.StringIO(up_file.read().decode()), delimiter=";")

            for row in data:
                Stats.objects.create(customer=row['Name'], film=row['Film'], watch_start=row['Start'], watch_end=row['End'])
                print(row['Name'], row['Film'], row['Start'], row['End'])

            for s in Stats.objects.all().values('film').annotate(count_users=Count('customer')):
                f = Film.objects.get(title=s['film'])
                f.count_users = s['count_users']
                f.save()


            for s in Stats.objects.all().values('film', 'customer').annotate(start=Min('watch_start'), end=Max('watch_end')):
                f = Film.objects.get(title=s['film'])
                f.watch_time += (s['end'] - s['start']).total_seconds() / 3600
                f.save()


            res['status'] = 'OK'
            return Response(res, status.HTTP_200_OK)
        except Exception as error:
            print(error)
            return Response(status.HTTP_404_NOT_FOUND)

    def post(self, request, filename, format=None):
        return self.put(request, filename, format)


class MoviesGet(FilmAPI):
    def get(self, request):
        res = {}
        res['resalt'] = []
        qs = Film.objects.all()
        qs_json = serializers.serialize('json', qs)
        for q in json.loads(qs_json):
            data = {}
            data['title'] = q['fields']['title']
            data['description'] = q['fields']['description']
            data['count users'] = q['fields']['count_users']
            data['watch time'] = q['fields']['watch_time']
            data['acters'] = []
            for act in  q['fields']['acters']:
                data['acters'].append(Acter.objects.get(id=act).name)
            res['resalt'].append(data)
        res['address'] = socket.gethostname()
        return Response(res, status.HTTP_200_OK)

