<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

use App\Log;

class LogController extends Controller
{
    public function logs()
    {
        $logs = Log::all();
        return view('/logs',compact('logs'));
    }

    public function create_log()
    {
    	
    }
}
