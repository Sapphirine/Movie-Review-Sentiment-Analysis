package log_analyzer;

import java.io.*;
import java.text.SimpleDateFormat;
import java.util.*;

public class TestFile {
     public static String readLog()
    {
        StringBuffer sb=new StringBuffer();
        String tempstr=null;
        try
        {
            String path="data/access.log";
            File file=new File(path);
            
            if(!file.exists())
                throw new FileNotFoundException();            
            	
            FileInputStream fis=new FileInputStream(file);
            
            BufferedReader br=new BufferedReader(new InputStreamReader(fis));
            
                       
            String MovieID;
            String IP;
            String Rating;
            String thisline=null;
            
            String arr[] = new String[200];
            int i = 0 ;
            
            while( (thisline=br.readLine())!=null )
            {

            	if(thisline.indexOf("movieid=")>=0 && thisline.indexOf("show_cart")>=0)
            	{
               		IP = thisline.substring(0, thisline.indexOf(" "));
            		arr[i]=IP;
            		i++;
            		
            		MovieID = thisline.substring(thisline.indexOf("movieid=")+8,
            				  thisline.indexOf("movieid=")+10);			
            		arr[i] = MovieID;
            	    i++;
            	    
            	    Rating ="3"; 
            		arr[i] = Rating;
            	    i++;
            	}
            	
                else if(thisline.indexOf("movieid=")>=0)
            	{
            		IP = thisline.substring(0, thisline.indexOf(" "));
            		arr[i]=IP;
            		i++;
            		
            		MovieID = thisline.substring(thisline.indexOf("movieid=")+8, 
            				  thisline.indexOf("movieid=")+10);
            		arr[i] = MovieID;
            	    i++;
            	    
            	    Rating ="5"; 
            		arr[i] = Rating;
            	    i++;
 
            	}

            	else 
            		System.out.println("Not found it!");
            }
            
            int arr_length = i;
            
            for (int j= 0 ; j < arr_length ; j++)
            {
            	arr[j] = arr[j].replace('"', ' ');	
            }
            
            
            //print out the unprocessed log file
            for (int j= 0 ; j < arr_length ; j++)
            {
            	System.out.println(arr[j]);	
            }
            
            //delete the redundant data
            
            for (int m = 1 ; m < arr_length ; m=m+3)
            {
            	
            	if (arr[m]==" ")
            		continue;
            	else
            	{
                	for (int n = m+3 ; n < arr_length ; n=n+3)
                	{
                		if(arr[n]!=" ")
                		{
                			if (arr[m].compareTo(arr[n])==0)
                    		{
                    			if(arr[m+1].compareTo(arr[n+1])==0)
                    			{
                    				arr[n-1] = " ";
                    				arr[n] = " ";
                    				arr[n+1] = " ";		
                    			}
                    			else if (arr[m+1].compareTo(arr[n+1])<0)
                    			{
                    				arr[m-1] = " ";
                    				arr[m] = " ";
                    				arr[m+1] = " ";
                    			}
                    			
                    			else
                    			{
                    				arr[n-1] = " ";
                    				arr[n] = " ";
                    				arr[n+1] = " ";

                    			}
                    		}
                			
                		}
                		else 
                		{
                			continue;
                		}
                	}

            	}
            	
            }
            
            
            //print out the processed log file
            for (int j= 0 ; j < arr_length ; j++)
            {
            	System.out.println(arr[j]);	
            }
            

        }
        
        catch(IOException ex)
        {
            System.out.println(ex.getStackTrace());
        }
        return sb.toString();
    }
    public static void main(String[] args) {
    	readLog();
    }

}