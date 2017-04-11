@extends('layouts.app')

@section('content')

<div class="container">
Tabla de Logs

<!-- Imprimir Usuarios desde la tabla-->

    <table class="tabla_usuarios">
        <tr>
            <th>id</th>
            <th>Fecha</th>
            <th>log_id</th>
             <th>detalles</th>
        </tr>
    @foreach ($logs as $log)
        <tr>
            <th>{{$log->id}}</th>
            <th>{{$log->created_at}}</th>
            <th>{{$log->log_id}}</th>
            <th>{{$log->content}}</th>
        </tr>
    @endforeach 
</div>
@endsection
