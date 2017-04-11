<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

use App\Tarjeta;
use File;
use App\Log;

class TarjetaController extends Controller
{
    public function tarjetas()
    {
        $tarjetas = Tarjeta::all();
        return view('/tarjetas',compact('tarjetas'));
    }

    public function create_card()
    {
    	$filename = 'card_number.txt';

    	$tarjeta = new Tarjeta;

    	// open file with the card number

    	$tarjeta->card_id = File::get($filename);
    	

    	//Check if there is not other card with the same number
    	$tarjeta1 = Tarjeta::where('card_id', '=', $tarjeta->card_id)->first();
    	if($tarjeta1 == null)
    	{
    		$tarjeta->save();

    		$log = new Log;
	    	$log->log_id = '9';
	    	$formato = 'Tarjeta  id: %s creada ';
	    	$log->content = sprintf($formato,$tarjeta->id);
	    	$log->save();
    	}
    	
    	
    	$tarjetas = Tarjeta::all();
    		return view('tarjetas',compact('tarjetas'));
    	//return view('home');
    }

     public function delete_card($id)
    {
    	//dd($id);

    	$tarjeta = Tarjeta::find($id);
    	$tarjeta->delete();
    	$tarjetas = Tarjeta::all();

    	$log = new Log;
    	$log->log_id = '11';
    	$formato = 'Tarjeta  id: %s eliminada ';
    	$log->content = sprintf($formato,$id);
    	$log->save();

    	return view('tarjetas',compact('tarjetas'));
    }

     public function modify_card($id)
    {

    	$tarjeta = Tarjeta::find($id);

    	if(request('new_user_id') != null)
    	{
    		$tarjeta->user_id = request('new_user_id');
    	}

    	$tarjeta->save();
    	$log = new Log;
    	$log->log_id = '10';
    	$formato = 'Tarjeta  id: %s re-asignada a usuario user_id: %s ';
    	$log->content = sprintf($formato,$tarjeta->id,$tarjeta->user_id);
    	$log->save();

    	$tarjetas = Tarjeta::all();

    	return view('tarjetas',compact('tarjetas'));
    }
}
