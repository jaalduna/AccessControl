@extends('layouts.app')

@section('content')

<div class="container">
Tabla de Tarjetas

<!-- Imprimir Usuarios desde la tabla-->

    <table class="tabla_usuarios">
        <tr>
            <th>id</th>
            <th>Numero</th>
            <th>id_usuario</th>
        </tr>
    @foreach ($tarjetas as $tarjeta)
        <tr>
            <th>{{$tarjeta->id}}</th>
            <th>{{$tarjeta->card_id}}</th>
            <th>{{$tarjeta->user_id}}</th>
             
            <th>
                <form action="/modify_card/{{$tarjeta->id}}" method="POST">
                    {{ csrf_field() }}  
                    <input type="text" name="new_user_id" class ="input_user_id" >
                    <button  type="submit" >modificar</button>
                </form>  
            </th>
            
                    
            <th>
                <form action="/delete_card/{{$tarjeta->id}}" method="POST">
                    {{ csrf_field() }}
                    <button  type="submit" >eliminar</button>
                </form>
            </th>
            
        </tr>
    @endforeach
        
    </table >
    <hr>
    <form action="/create_card" method="POST">
        {{ csrf_field() }}  
                    <th><button  type="submit" >agregar</button></th>
    </form>
</div>
@endsection
