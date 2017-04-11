@extends('layouts.app')

@section('content')

<div class="container">
Tabla de Usuarios

<!-- Imprimir Usuarios desde la tabla-->

    <table class="tabla_usuarios">
        <tr>
            <th>id</th>
            <th>nombre</th>
            <th>apellido</th>
            <th>rut</th>
            <th>habilitado</th>
        </tr>
    @foreach ($users as $usuario)
        <tr>
            <th>{{$usuario->id}}</th>
            <th>{{$usuario->name}}</th>
            <th>{{$usuario->second}}</th>
            <th>{{$usuario->rut}}</th>
            <th>{{$usuario->enabled}}</th>
             
            <th>
                <form action="/modify_user/{{$usuario->id}}" method="POST">
                    {{ csrf_field() }}  
                    <button  type="submit" >modificar</button>
                </form>  
            </th>
            
                    
            <th>
                <form action="/delete_user/{{$usuario->id}}" method="POST">
                    {{ csrf_field() }}
                    <button  type="submit" >eliminar</button>
                </form>
            </th>
            
        </tr>
    @endforeach
        
    </table >
    <hr>
    <form action="/create_user" method="POST">
        {{ csrf_field() }}  
        <table class="tabla_usuarios">
        <tr>
             <th>nombre</th>
            <th>apellido</th>
            <th>rut</th>
            <th>habilitado</th>
        </tr>
                <tr>
                    <th><input type="text" id="name" name="name"></th>
                    <th><input type="text" id="second" name="second"></th>
                    <th><input type="text" id="rut" name="rut"></th>
                    <th><input type="text" id="enabled" name="enabled"></th>
                    <th><button  type="submit" >agregar</button></th>
                </tr>
        </table>
    </form>
</div>
@endsection
