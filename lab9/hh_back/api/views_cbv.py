class VacancyDetail(APIView):
    def get(self, request, pk):
        try:
            vacancy = Vacancy.objects.get(pk=pk)
        except Vacancy.DoesNotExist:
            return Response(status=404)
        serializer = VacancyCustomSerializer(vacancy)
        return Response(serializer.data)
