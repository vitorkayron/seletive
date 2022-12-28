from django.db import models

class Tecnologia(models.Model):
    tecnologia = models.CharField(max_length=30)

    def __str__(self):
        return self.tecnologia

class Empresa(models.Model):
    choices_nicho_mercado = (
        ('M', 'Marketing'),
        ('N', 'Nutrição'),
        ('D', 'Design'),
        ('T', 'Tecnologia'),
        ('A', 'Advocacia'),
    )

    logo = models.ImageField(upload_to="logo_empresa")
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    cidade = models.CharField(max_length=30)
    tecnologia = models.ManyToManyField(Tecnologia)
    endereco = models.CharField(max_length=60)
    nicho_mercado = models.CharField(max_length=50, choices=choices_nicho_mercado)
    caracteristica_empresa = models.TextField()

    def __str__(self):
        return self.nome

    def qtd_vagas(self):
        return Vaga.objects.filter(empresa__id=self.id).count()

class Vaga(models.Model):
    choices_experiencia = (
        ('E', 'Estágio'),
        ('J', 'Júnior'),
        ('P', 'Pleno'),
        ('S', 'Sênior')
    )

    choices_status = (
        ('I', 'Interesse'),
        ('C', 'Currículo enviado'),
        ('E', 'Entrevista'),
        ('D', 'Desafio técnico'),
        ('F', 'Finalizado')
    )
    
    empresa = models.ForeignKey(Empresa, on_delete=models.DO_NOTHING)
    titulo = models.CharField(max_length=30)
    nivel_experiencia = models.CharField(max_length=2, choices=choices_experiencia)
    data_final = models.DateField()
    email = models.EmailField(null=True)
    status = models.CharField(max_length=30, choices=choices_status)
    tecnologia_dominadas = models.ManyToManyField(Tecnologia)
    tecnologia_estudar = models.ManyToManyField(Tecnologia, related_name='estudar')

    def progresso(self):
        x = [((i+1)*20,j[0]) for i, j in enumerate(self.choices_status)]
        x = list(filter(lambda x: x[1] == self.status, x))[0][0]
        return x


    def __str__(self):
        return self.titulo