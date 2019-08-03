require 'fileutils'

train_data_path = "./data/train/data.txt"
test_data_path = "./data/test/data.txt"

FileUtils.touch(train_data_path) unless FileTest.exist?(train_data_path)
FileUtils.touch(test_data_path) unless FileTest.exist?(test_data_path)


test_kim_data_paths = Dir.glob("./data/test/kim/*.jpg")
test_tel_data_paths = Dir.glob("./data/test/tel/*.jpg")
test_other_data_paths = Dir.glob("./data/test/other/*.jpg")
train_kim_data_paths = Dir.glob("./data/train/kim/*.jpg")
train_tel_data_paths = Dir.glob("./data/train/tel/*.jpg")
train_other_data_paths = Dir.glob("./data/train/other/*.jpg")


File.open(test_data_path, "w") do |f|
  test_kim_data_paths.each { |path| f.puts("#{path} 0") }
  test_tel_data_paths.each { |path| f.puts("#{path} 1") }
  test_other_data_paths.each { |path| f.puts("#{path} 2") }
end
File.open(train_data_path, "w") do |f|
  train_kim_data_paths.each { |path| f.puts("#{path} 0") }
  train_tel_data_paths.each { |path| f.puts("#{path} 1") }
  train_other_data_paths.each { |path| f.puts("#{path} 2") }
end
