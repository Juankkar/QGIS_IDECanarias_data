# Leemos el CSV de los metadatos, y obtenemos la columna de "url"
$data = Get-Content -Path "..\metadata\metadatos_medio_ambiente.csv" | ForEach-Object { ($_ -split ',')[3] } | Where-Object { $_ -notlike "*url*" }

$downloadDirectory = "..\data"

# Si el downloadDirectory no existe lo creamos
if (-not (Test-Path -Path $downloadDirectory -PathType Container)) {
    New-Item -ItemType Directory -Force -Path $downloadDirectory
}

# Descargamos los archivos
foreach ($i in $data) {
    Invoke-WebRequest -Uri $i -OutFile (Join-Path -Path $downloadDirectory -ChildPath (Split-Path -Path $i -Leaf))
}

# Una vez descargados, se extraeran los archivos de los ZIP
$zipFiles = Get-ChildItem -Path $downloadDirectory -Filter *.zip
foreach ($zipFile in $zipFiles) {
    Expand-Archive -Path $zipFile.FullName -DestinationPath $downloadDirectory -Force
}
