<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;
use App\Log;

class LogController extends Controller
{
    public function logs()
    {
        $logs = DB::table('logs')->orderBy('id','desc')->get();
        return view('/logs',compact('logs'));
    }

    public function create_log()
    {
    	
    }
}
