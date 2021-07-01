from rest_framework import serializers


class FilterCommentListSerializer(serializers.ListSerializer):
    """ Фильтр комментариев, только parents"""
    def to_representation(self, data):
        data = data.filter(parent=None)  # фильтруем кометратии. Из любоко списка кометариев будем получать только родителей
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):   # рекурсивный вывод коментов

    """ Вывод рекурсивно children
    """
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data
