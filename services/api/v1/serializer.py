from rest_framework import serializers
from services.models import Services , Comments , Category , Special_services
from accounts.models import User



class ServiceSerializer(serializers.ModelSerializer):
    # category = serializers.SlugRelatedField(many=True , queryset=Category.objects.all(),slug_field="title")
    # specials = serializers.SlugRelatedField(many=True , queryset=Special_services.objects.all(),slug_field="service")

    class Meta:
        model = Services
        fields = "__all__"


    def to_representation(self, instance):
        rep = super().to_representation(instance)
        cat = []
        for category_id in rep["category"]:
            title = Category.objects.get(id=category_id).title
            cat.append(title)
        rep["category"] = cat
        return rep



class CommentSerializer(serializers.ModelSerializer):

    status = serializers.SerializerMethodField(method_name="edit_status")
    service = serializers.SerializerMethodField(method_name="edit_service")
    name = serializers.SerializerMethodField(method_name="edit_name")


    class Meta:
        model = Comments
        fields = ["service","name","status" , "message"]
        read_only_fields = ["service","name","status"]

    def edit_status(self,instance):
        if instance.status == True:
            return "Approve"
        else:
            return "Not-approve"
        

    def edit_service(self,instance):
        id = instance.service.id
        tittle = Services.objects.get(id=id).title
        return tittle
    

    def edit_name(self,instance):
        id = instance.name.id
        name = User.objects.get(id=id).email
        return name
        