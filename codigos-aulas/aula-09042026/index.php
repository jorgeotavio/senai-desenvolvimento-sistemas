<?php

header('Access-Control-Allow-Origin: *');

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

if($usuarioValido != null) {
    echo json_encode($usuarioValido);
    exit;
}


echo "Erro";

