<?php
$bancoDeDados = [
    [
        'user' => 'juliana',
        'password' => 'minatoeabel',
        'color' => 'purple'
    ],
    [
        'user' => 'alexandre',
        'password' => 'alexandreogrande',
        'color' => 'pink'
    ]
];

$user = $_GET['user'];
$password = $_GET['password'];

$usuarioValido = null;

foreach ($bancoDeDados as $userDb) {
    if ($user == $userDb['user'] && $password == $userDb['password']) {
        $usuarioValido = $userDb;
    }
}

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <style>
        h5 {
            color: <?php echo $usuarioValido['color'] ?>;
        }
    </style>
    <div>
        <h5>
            <!-- comentario  -->
            <?php
                if($usuarioValido != null) {
                    echo "Boas-vindas $usuarioValido[user]";
                } else {
                    echo "Usuário Inválido";
                }            
            ?> 
        </h5>
    </div>
    <script>
        let nome = "<?php echo $user ?>"
    </script>
</body>
</html>