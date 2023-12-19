# https://askubuntu.com/a/1365053/987368

if [ $# -lt 1 ];
then
    echo "Provide input file as first argument"
    exit 1
fi

export out_dir=`(dirname $1)`
export out_file="$out_dir/$(basename $1 .png).ico"
export file_name="$(basename $1 .png).ico"
echo $out_file

if [ $# -eq 1 ];
then
    convert $1 -define icon:auto-resize=256,128,64,48,32,16 $out_file
elif [ $# -eq 2 ];
then
     convert $1 -define icon:auto-resize=256,128,64,48,32,16 $2/$file_name
else
    echo "Currently only one file to be provided"
fi
