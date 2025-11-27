from django.db import models


class Planta(models.Model):
    nome_cientifico = models.CharField(max_length=150)
    nome_popular = models.CharField(max_length=150, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    
    imagem = models.ImageField(upload_to='plantas/', blank=True, null=True)
    
    risco_extincao = models.BooleanField(default=False)
    data_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome_cientifico


class UsoMedicinal(models.Model):
    planta = models.ForeignKey(Planta, on_delete=models.CASCADE, related_name='usos_medicinais')
    
    parte_utilizada = models.CharField(max_length=100)       # exemplo: folhas, raiz, caule
    modo_preparo = models.CharField(max_length=200)          # exemplo: infusão, decocção, maceração
    indicacao = models.CharField(max_length=200)             # exemplo: dores, inflamação, febre, etc.

    def __str__(self):
        return f"{self.planta.nome_cientifico} - {self.indicacao}"


class Regiao(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField(blank=True, null=True)
    tipo_bioma = models.CharField(max_length=100, default='Cerrado')

    # muitas regiões podem ter muitas plantas
    plantas = models.ManyToManyField(Planta, related_name='regioes', blank=True)

    def __str__(self):
        return self.nome

    
class FonteCientifica(models.Model):
    planta = models.ForeignKey(
        Planta,
        on_delete=models.CASCADE,
        related_name='fontes_cientificas'
    )

    titulo = models.CharField(max_length=255)
    autores = models.CharField(max_length=255)
    ano = models.PositiveIntegerField()
    fonte = models.CharField(max_length=255)
    link = models.URLField(blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.titulo} ({self.ano})"

