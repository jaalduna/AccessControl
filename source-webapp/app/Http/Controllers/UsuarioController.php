<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Usuario;
use App\Log;

class UsuarioController extends Controller
{
    public function modify_user($id)
    {
    	//dd($id);

    	$user = Usuario::find($id);
    	if($user->enabled){
    		$user->enabled = 0;

    		$log = new Log;
		    $log->log_id = '7';
		    $formato = 'Usuario id: %s deshabilitado ';
		    $log->content = sprintf($formato,$user->id);
		    $log->save();   
    	}
    	else{
    		$user->enabled = 1;
    		$log = new Log;
		    $log->log_id = '7';
		    $formato = 'Usuario id: %s habilitado ';
		    $log->content = sprintf($formato,$user->id);
		    $log->save(); 
    	}
    	$user->save();

    	 	
    	$users = Usuario::all();


    	return view('usuarios',compact('users'));
    }

     public function delete_user($id)
    {
    	//dd($id);

    	$user = Usuario::find($id);
    	$user->delete();
    	$users = Usuario::all();

    	$log = new Log;
    	$log->log_id = '8';
    	$formato = 'Usuario id: %s eliminado ';
    	$log->content = sprintf($formato,$id);
    	$log->save();

    	return view('usuarios',compact('users'));
    }

    public function create_user()
    {
    	//dd($id);

    	$user = new Usuario;
    	$user->name = request('name');
    	$user->second = request('second');
    	$user->rut = request('rut');
    	$user->enabled = request('enabled');

    	//Check if there is not other user with the same rut
    	$user1 = Usuario::whereExist('rut', '=', request('rut'))->first();
    	if($user1 == null)
    	{
    		$user->save();

    		$log = new Log;
	    	$log->log_id = '6';
	    	$formato = 'Usuario id: %s creado ';
	    	$log->content = sprintf($formato,$user->id);
	    	$log->save();
    	}
    
    	$users = Usuario::all();
    		return view('usuarios',compact('users'));
    	
    	//return view('home');
    }
}
